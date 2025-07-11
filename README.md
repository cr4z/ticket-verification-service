# Ticket Verification Service

A simple microservice that verifies ticket IDs against a predefined dataset. Part of my cloud application Flexiserver, a collection of microservices for demo use that share a rate limited API gateway at 500req/hour for cost management.

## Usage

**Endpoint:** `GET /verify/{id}`

**Example:**
```bash
curl https://flexiserver-561525660706.us-central1.run.app/a1b2c3d4e5f6
```

**Response:**
```json
{
  "valid": true
}
```

## Valid Test IDs

The service recognizes these test ticket IDs:
- `a1b2c3d4e5f6`
- `9876543210ab`
- `fedcba098765`
- `123456789abc`
- `def456789012`
