# Project Title

This project offers a specialized feature: the dynamic generation of schema definition JSON files.
Its primary objective is to simplify and accelerate the creation of these files crucial for broker deployment.
By providing a Django-powered API, it enables swift management of RabbitMQ configurations, easing the process of obtaining comprehensive schema definitions required for efficient and rapid broker setup.

## Description

This project provides a Django-based API to manage RabbitMQ configurations and generate a schema definition file in JSON format.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    ```bash
    python manage.py migrate
    ```

## Models

### RabbitMQInfo

- `version`: CharField, max_length=50
- `cluster_name`: CharField, max_length=100

### Vhost

- `name`: CharField, max_length=100, unique=True

### User

- `username`: CharField, max_length=100, unique=True
- `password`: CharField, max_length=100

### Permission

- `user`: ForeignKey to User, on_delete=models.CASCADE
- `vhost`: ForeignKey to Vhost, on_delete=models.CASCADE
- `configure`: CharField, max_length=50, default='.*'
- `write`: CharField, max_length=50, default='.*'
- `read`: CharField, max_length=50, default='.*'

### Queue

- `name`: CharField, max_length=100
- `vhost`: ForeignKey to Vhost, on_delete=models.CASCADE

### Exchange

- `name`: CharField, max_length=100
- `vhost`: ForeignKey to Vhost, on_delete=models.CASCADE

### Binding

- `source`: ForeignKey to Exchange, on_delete=models.CASCADE, related_name='source_bindings'
- `destination`: ForeignKey to Exchange, on_delete=models.CASCADE, related_name='destination_bindings'
- `destination_type`: CharField, max_length=100
- `routing_key`: CharField, max_length=100

## URLs and Endpoints

### API Endpoints

The project exposes the following API endpoints:

- `vhosts/`: Retrieve, create, update, or delete Virtual Hosts.
- `users/`: Retrieve, create, update, or delete Users.
- `permissions/`: Retrieve, create, update, or delete Permissions.
- `queues/`: Retrieve, create, update, or delete Queues.
- `exchanges/`: Retrieve, create, update, or delete Exchanges.
- `bindings/`: Retrieve, create, update, or delete Bindings.

### Usage

To access the API endpoints, use the following URLs:

- `http://your-domain.com/vhosts/`
- `http://your-domain.com/users/`
- `http://your-domain.com/permissions/`
- `http://your-domain.com/queues/`
- `http://your-domain.com/exchanges/`
- `http://your-domain.com/bindings/`

### Schema Generation

To generate the schema definition JSON file, use:

- `http://your-domain.com/generator/`

This will produce a `schema.definitions.json` file.

## Contributing

To contribute, please contact Jorge Rubio at jorge95jrc@gmail.com.

## License

This project is licensed under the MIT License.