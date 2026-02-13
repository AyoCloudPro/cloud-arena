resource "google_artifact_registry_repository" "repo" {
  location      = var.region
  repository_id = var.service_name
  description   = "Docker repository for Cloud Arena"
  format        = "DOCKER"
}


resource "google_cloud_run_v2_service" "service" {
  name     = var.service_name
  location = var.region
  ingress = "INGRESS_TRAFFIC_ALL"
  deletion_protection = false

  template {
    containers {
      image = var.image_name

      ports {
        container_port = 8080
      }

      env {
        name  = "CLOUD_PROVIDER"
        value = "GCP"
      }

      env {
        name  = "REGION"
        value = var.region
      }

      env {
        name  = "ENVIRONMENT"
        value = "prod"
      }

      env {
        name  = "DOCKER_IMAGE"
        value = var.image_name
      }

      env {
        name  = "BUILD_NUMBER"
        value = "manual"
      }
    }
  }

  traffic {
    percent = 100
    type    = "TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST"
  }

  depends_on = [
    google_artifact_registry_repository.repo
  ]
}


resource "google_cloud_run_v2_service_iam_member" "public_access" {
  name     = google_cloud_run_v2_service.service.name
  location = google_cloud_run_v2_service.service.location
  role     = "roles/run.invoker"
  member   = "allUsers"
}