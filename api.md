# Users

Types:

```python
from ronnie_beeceptor_api.types import User, UserListResponse
```

Methods:

- <code title="post /users">client.users.<a href="./src/ronnie_beeceptor_api/resources/users.py">create</a>(\*\*<a href="src/ronnie_beeceptor_api/types/user_create_params.py">params</a>) -> <a href="./src/ronnie_beeceptor_api/types/user.py">User</a></code>
- <code title="get /users/{userId}">client.users.<a href="./src/ronnie_beeceptor_api/resources/users.py">retrieve</a>(user_id) -> <a href="./src/ronnie_beeceptor_api/types/user.py">User</a></code>
- <code title="get /users">client.users.<a href="./src/ronnie_beeceptor_api/resources/users.py">list</a>() -> <a href="./src/ronnie_beeceptor_api/types/user_list_response.py">UserListResponse</a></code>
