swagger: "2.0"
info:
  description: ""
  version: "0.0.1"
  title: "Todo-Listen-Verwaltung"
  contact:
    email: "jannik.bauer@bohnenkamp.de"
  license:
    name: "Apache 2.0"
    url: "http://www.apache.org/licenses/LICENSE-2.0.html"
host: "127.0.0.1:5000"
basePath: "/"
tags:
- name: "Listenverwaltung"
schemes:
- "http"
paths:
  /list/{list_id}:
    get:
      summary: "Get all items from list"
      description: ""
      tags:
      - Listenverwaltung
      operationId: "getList"
      produces:
      - "application/json"
      parameters:
      - in: "path"
        name: "list_id"
        type: string
        description: "list id"
        required: true
      responses:
        "200":
          description: "List item returned"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TodoEntry"
        "404":
          description: "Invalid list id"
    delete:
      summary: "Delete a list"
      description: ""
      tags:
      - Listenverwaltung
      operationId: "deleteList"
      produces:
      - "application/json"
      parameters:
      - in: "path"
        name: "list_id"
        type: string
        description: "list id"
        required: true
      responses:
        "200":
          description: "List was deleted"
        "404":
          description: "Invalid list id"
  /list:
    post:
      summary: "Add new list"
      description: ""
      tags:
      - Listenverwaltung
      operationId: "addList"
      produces:
      - "application/json"
      consumes:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        description: "list object"
        required: true
        schema:
          $ref: "#/definitions/TodoList"
      responses:
        "200":
          description: "List added"
          schema:
            $ref: "#/definitions/TodoList"
        "500":
          description: "List could not be added"
definitions:
  TodoList:
    type: "object"
    properties:
      id:
        type: "string"
        format: "uuid"
      name:
        type: "string"
  TodoEntry:
    type: "object"
    properties:
      id:
        type: "string"
        format: "uuid"
      name:
        type: "string"
      description:
        type: "string"
      user_id:
        type: "string"
        format: "uuid"
      list_id:
        type: "string"
        format: "uuid"