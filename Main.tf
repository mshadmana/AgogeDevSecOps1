provider "aws" {
  region = "eu-west-2" # London region
}
resource "aws_s3_bucket" "terraformseptbucketsun13" {
  bucket = "terraformseptbucketsun13"
}
terraform {
  backend "s3"{
    bucket ="terraformseptbucketsun13"
    key = "global/s3/terraform.tfstate"
    region = "eu-west-2"
  }
  
}