resource "aws_elasticache_replication_group" "ringnode" {
  replication_group_id          = "ringnode-prod"
  description                   = "Ringnode subscriber session store"
  engine                        = "redis"
  num_cache_clusters            = 2
  node_type                     = "cache.t3.medium"

  # RNG-IAC-001: TLS not required.
  transit_encryption_enabled = false
  # RNG-IAC-002: no AUTH token.
  # auth_token = ...   <-- intentionally omitted
}
