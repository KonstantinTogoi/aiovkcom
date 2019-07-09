from .exceptions import APIError

import aiohttp


class Session:
    """A wrapper around aiohttp.ClientSession."""

    CONTENT_TYPE = 'application/json; charset=utf-8'

    __slots__ = ('session', )

    def __init__(self, session=None):
        self.session = session or aiohttp.ClientSession()

    def __await__(self):
        return self.authorize().__await__()

    async def __aenter__(self):
        return await self.authorize()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def authorize(self):
        return self

    async def close(self):
        await self.session.close()


class TokenSession(Session):
    """Session for sending authorized requests."""

    URL = 'https://api.vk.com/method/'
    V = '5.101'

    __slots__ = ('access_token', 'v')

    def __init__(self, access_token, v='', session=None):
        super().__init__(session)
        self.access_token = access_token
        self.v = v or self.V

    @property
    def required_params(self):
        """Required parameters."""
        return {'v': self.v, 'access_token': self.access_token}

    async def request(self, method_name, params=()):
        """Sends a request.

        Args:
            method_name (str): method's name.
            params (dict): URL parameters.

        Returns:
            response (dict): JSON object response.

        """

        url = f'{self.URL}/{method_name}'
        params = {k: params[k] for k in params if params[k]}
        params.update(self.required_params)

        async with self.session.get(url, params=params) as resp:
            status = resp.status
            response = await resp.json(content_type=self.CONTENT_TYPE)

        if status == 200:
            response = response['response']
        else:
            raise APIError(response['error'])

        return response


class ImplicitSession(TokenSession):

    OAUTH_URL = 'https://oauth.vk.com/authorize'
    REDIRECT_URI = 'https://oauth.vk.com/blank.html'

    __slots__ = ('client_id', 'login', 'passwd', 'scope')

    def __init__(self, client_id, login, passwd, scope='', v='', session=None):
        super().__init__('', v, session)
        self.client_id = client_id
        self.login = login
        self.passwd = passwd
        self.scope = scope

    @property
    def params(self):
        """Authorization parameters."""
        return {
            'client_id': self.client_id,
            'display': 'page',
            'redirect_uri': self.REDIRECT_URI,
            'response_type': 'token',
            'scope': self.scope,
            'v': self.v,
        }
