provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "ecommerce_server" {
  ami           = "ami-0abcdef1234567890"  # Replace with the latest AMI ID
  instance_type = "t2.micro"
  key_name      = var.key_name
  tags = {
    Name = "ecommerce-server"
  }
}

resource "aws_security_group" "ecommerce_sg" {
  name_prefix = "ecommerce-sg"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
