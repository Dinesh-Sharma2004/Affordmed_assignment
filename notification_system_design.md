# Notification System Design

## Introduction

The Notificaiton System is a simple backend service developed using Flask and SQLAlchemy.

Its main purpose is to:
-Create notifications
-Fetch notifications
-Marks notifications
-Delete notifications
-Manage unread notificaions

The system follows a clean modular backend structure for maintainability and scalability.

## Architecture
 Simple Flask Backend Application

 ## Components

 -Flask
 -SQLAlchemy
 -SQLite
 -Logging Middleware

 ## APIs

 -GET /notifications
 -GET /notificaitons/unread
 -POST /noitfications/send
 -PATCH /notifications/<id>/read
 -PATCH /notifications/<id>

 ## Logging Middleware

 Implemented using:
 -before_request
 -after_request

