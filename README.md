# Python code for 'Logs Analysis' Udacity project

## Purpose

This application is an internal reporting tool that analyzes a database consisting of newspaper articles, author information, and user log.

The application reports the three most popular articles, the most popular authors, and days where the error rate exceeded 1%.

## Installation

To run this application the following must be done:

1) Install VirtualBox from virtualbox.org

2) Install Vagrant from vagrantup.com

3) Download the VM configuration from https://github.com/udacity/fullstack-nanodegree-vm

4) Change directory to the 'vagrant' directory

5) Download 'newsdata.sql' from https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91

6) Run 'vagrant up'

7) Run 'vagrant ssh'

8) Run 'psql -d news -f newsdata.sql'

9) Copy 'log_analysis.py' to 'vagrant' directory

## Command to Run

'python log_analysis.py'
