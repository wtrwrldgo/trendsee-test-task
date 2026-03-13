# /test-api — Test All API Endpoints

Run through all API endpoints to verify they work.

## Steps
1. Create a test user via `POST /users`
2. Extract JWT token from response
3. Test `GET /users/{id}/token`
4. Test `PATCH /users/{id}` with auth
5. Create a publication via `POST /publications` with auth
6. Test `GET /publications/user/{id}` — verify pagination
7. Test `PATCH /publications/{id}` with auth
8. Test `DELETE /publications/{id}` with auth
9. Test `DELETE /users/{id}` with auth
10. Report pass/fail for each endpoint
