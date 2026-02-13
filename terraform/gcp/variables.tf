variable "project_id" {
    type = string
}

variable "region" {
    type = string
    default = "us-central1"
}

variable "service_name" {
    type = string
    default = "cloud-arena"
}

variable "image_name" {
    type = string
}

variable "sa_key" {
    sensitive = true
}