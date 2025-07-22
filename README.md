# Python Automations

## Overview

This repository contains a growing collection of practical Python scripts designed to automate everyday tasks.

Each script is modular, well-documented, and uses Python's standard library wherever possible — making them lightweight, secure, and easy to run.

## Scripts Included




| Script                          | Description                                                                         |
|-------------------------------|---------------------------------------------------------------------------------------|     
| disk_usage_email_alert.py      | Sends email if disk usage exceeds threshold                                          |
| backup_folder.py               | Creates zip backups of target folder                                                 |
| rename_bulk_files.py           | Renames files in bulk using custom pattern                                           |
| s3_backup_uploader.py          | Uploads .zip files to AWS S3 with tags and error handling                            |
| nightly_ec2_shutdown.py        | Stops EC2 instances tagged `Shutdown=true` every 5 minutes via EventBridge Scheduler |
| cross_account_s3.py            | Assumes IAM role in another AWS account to access S3 bucket and list stored objects  |

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/python_automations.git
   cd python_automations/scripts
