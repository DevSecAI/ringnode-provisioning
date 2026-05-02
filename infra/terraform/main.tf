provider "aws" { region = "eu-west-2" }

resource "aws_vpc" "ringnode" { cidr_block = "10.70.0.0/16" }

# RNG-IAC-003: Redis port open to the world.
resource "aws_security_group" "redis" {
  name   = "ringnode-redis"
  vpc_id = aws_vpc.ringnode.id
  ingress {
    from_port   = 6379
    to_port     = 6379
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
