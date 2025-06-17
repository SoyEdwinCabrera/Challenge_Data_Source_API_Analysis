# Error Handling & Troubleshooting for GitHub API

This document outlines the most common errors encountered while interacting with the GitHub API, and the strategies used to detect, debug, and resolve them.

---

## 1. Authentication Errors (401 Unauthorized)

**Description**: This occurs when the authentication token is missing, invalid, or lacks proper scope.

![401_Error](../Assets/401_Error.png)

**Common Causes**:
- Missing `Authorization` header.
- Expired or revoked token.
- Incorrect token format (e.g., `token <your_token>` missing "token" prefix).
- Token lacks required scopes for certain endpoints.

**Solution**:
- Double-check token format in headers:  
  `Authorization: token YOUR_PERSONAL_ACCESS_TOKEN`
- Regenerate the token from GitHub if expired.
- Ensure the token has proper scopes (e.g., `repo`, `read:org`, etc.).

---

## 2. Rate Limit Errors (403 Forbidden)

**Description**: GitHub enforces rate limits depending on whether you are authenticated or not.

**Common Causes**:
- Too many requests in a short period.
- Unauthenticated requests reaching the limit (60 requests/hour).
- Authenticated requests exceeding 5,000 requests/hour.

**Solution**:
- Authenticate your requests to access the higher rate limit.
- Monitor headers:
  - `X-RateLimit-Limit`
  - `X-RateLimit-Remaining`
  - `X-RateLimit-Reset`
- Implement a cooldown (e.g., `time.sleep()`) when the limit is near.

---

## 3. Not Found Errors (404)

![404_Error](../Assets/404_Error.png)

**Description**: The requested resource does not exist or is not accessible to the user/token.

**Common Causes**:
- Typo in the endpoint URL.
- Accessing private data with a token lacking permission.
- Wrong owner/repo name in the request.

**Solution**:
- Double-check the full request URL.
- Make sure the authenticated user has access to the resource.
- Test the URL in the browser or with curl to verify availability.

---
