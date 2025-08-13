from httpx import Request, Response
from tools.logger import get_logger

logger = get_logger('HTTP_CLIENT')

async def log_request_event_hook(request: Request):
    logger.info(f'Mke {request.method} request to {request.url}')

async def log_respose_event_hook(response: Response):
    logger.info(
        f"Got response {response.status_code} {response.reason_phrase} from {response.url}"
    )