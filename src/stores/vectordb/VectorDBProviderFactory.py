from .providoers.QdrantDBProvider import QdrantDBProvider
from .providoers.PGVectorProvider import PGVectorProvider
from .providoers.SupabaseVectorProvider import SupabaseVectorProvider
from .VectorDBEnums import VectorDBEnums
from controllers.BaseController import BaseController


class VectorDBProviderFactory:
    def __init__(self, config, db_client: object = None):
        self.config = config
        self.base_controller = BaseController()
        self.db_client = db_client

    def create_provider(self, provider: str):
        if provider == VectorDBEnums.QDRANT.value:
            qdrant_db_client = self.base_controller.get_database_path(db_name=self.config.VECTOR_DB_PATH)

            return QdrantDBProvider(
                db_client=qdrant_db_client,
                distance_method=self.config.VECTOR_DB_DISTANCE_METHOD,
                default_vector_size=self.config.EMBEDDING_MODEL_SIZE or self.config.VECTOR_DB_DEFAULT_VECTOR_SIZE,
                index_threshold=self.config.VECTOR_DB_INDEX_THRESHOLD,
            )

        if provider == VectorDBEnums.PGVECTOR.value:
            return PGVectorProvider(
                db_client=self.db_client,
                distance_method=self.config.VECTOR_DB_DISTANCE_METHOD,
                default_vector_size=self.config.EMBEDDING_MODEL_SIZE or self.config.VECTOR_DB_DEFAULT_VECTOR_SIZE,
                index_threshold=self.config.VECTOR_DB_INDEX_THRESHOLD,
            )

        if provider == VectorDBEnums.SUPABASE.value:
            return SupabaseVectorProvider(
                distance_method=self.config.VECTOR_DB_DISTANCE_METHOD,
                default_vector_size=self.config.EMBEDDING_MODEL_SIZE or self.config.VECTOR_DB_DEFAULT_VECTOR_SIZE,
            )
        
        return None



