import aiohttp
import logging
from asyncio import TimeoutError
from aiohttp import ClientError

logger = logging.getLogger(__name__)


async def get_text(url: str) -> str | None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if 400 <= resp.status < 500:
                    logger.error("Client error")
                elif resp.status > 500:
                    logger.error("server error")
                else:
                    return await resp.text()
    except ClientError as ex:
        logger.error(f"There are problems with connection {ex}")
    except TimeoutError as ex:
        logger.error(f"Timeout error {ex}")


def prepare_matrix(text: str) -> list[list[int]]:
   try:
        matrix = []
        for line in text.split('\n'):
            if line and line[0] != '+':
                matrix.append([int(num) for num in line[1:-1].split('|')])

        if matrix and not all([len(matrix) == len(line) for line in matrix]):
            raise ValueError("Matrix is not squared")
   except ValueError as ex:
        logger.warning(ex)
        return []
   return matrix


def traverse_matrix(matrix: list[list[int]], output: list[int] = None) -> list[int]:
    if output is None:
        output = []
    if not len(matrix):
        return output
    matrix = list(zip(*matrix[::-1]))
    output.extend(matrix[0][::-1])
    traverse_matrix(matrix[1:], output)


async def get_matrix(url: str) -> list[int]:
    output = []
    text = await get_text(url)
    traverse_matrix(prepare_matrix(text), output)
    return output