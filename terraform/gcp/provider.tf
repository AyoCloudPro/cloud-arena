terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "7.19.0"
    }
  }
}

provider "google" {
  # Configuration options
  project = var.project_id
  region = var.region
  credentials = var.sa_key
}

