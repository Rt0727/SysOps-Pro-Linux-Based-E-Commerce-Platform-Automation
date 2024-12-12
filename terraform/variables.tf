variable "key_name" {
  description = "The name of the EC2 key pair"
  type        = string
}

variable "instance_type" {
  description = "The type of the EC2 instance"
  type        = string
  default     = "t2.micro"
}
