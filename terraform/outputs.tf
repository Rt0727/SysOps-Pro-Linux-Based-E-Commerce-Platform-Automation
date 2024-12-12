output "public_ip" {
  value = aws_instance.ecommerce_server.public_ip
}

output "private_ip" {
  value = aws_instance.ecommerce_server.private_ip
}
