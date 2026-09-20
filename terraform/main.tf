# Terraform Configuration - AWS
# Contains intentional security misconfigurations for scanning demo

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "eu-west-2"
}

# Vulnerability 1: S3 bucket with public access protections disabled
resource "aws_s3_bucket" "vulnerable_bucket" {
  bucket = "devsecops-demo-bucket-vulnerable"

  tags = {
    Name        = "Vulnerable Demo Bucket"
    Environment = "Demo"
  }
}

resource "aws_s3_bucket_public_access_block" "vulnerable_bucket_pab" {
  bucket = aws_s3_bucket.vulnerable_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# Vulnerability 2: Security group allowing all traffic
resource "aws_security_group" "vulnerable_sg" {
  name        = "vulnerable-security-group"
  description = "Intentionally vulnerable security group"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Vulnerability 3: EC2 instance with insecure configuration
resource "aws_instance" "vulnerable_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.vulnerable_sg.id]

  associate_public_ip_address = true

  root_block_device {
    encrypted = false
  }

  user_data = <<-USERDATA
              #!/bin/bash
              export DB_PASSWORD="hardcoded_password"
              echo "Setting up application..."
              USERDATA

  tags = {
    Name = "Vulnerable Instance"
  }
}
