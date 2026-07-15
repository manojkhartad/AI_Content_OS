from services.service_registry import SERVICE_REGISTRY


class ServiceFactory:

    @staticmethod
    def create(name: str):

        if name not in SERVICE_REGISTRY:
            raise ValueError(
                f"Unknown service: {name}"
            )

        service_class = SERVICE_REGISTRY[name]

        return service_class()