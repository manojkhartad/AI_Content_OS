from services.base_service import BaseService


SERVICE_REGISTRY: dict[str, type[BaseService]] = {}