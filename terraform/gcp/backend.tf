terraform { 
  cloud { 
    
    organization = "digitalmages" 

    workspaces { 
      name = "cloud_arena" 
    } 
  } 
}