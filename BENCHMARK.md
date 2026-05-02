# Ringnode — Seeded Findings (23 total)

## SAST (10)
| ID | CWE | File | Description |
|---|---|---|---|
| RNG-SAST-001 | CWE-1336 | `ringnode/templates.py` (`render_template_string` on user input) |
| RNG-SAST-002 | CWE-489  | `ringnode/app.py` (`debug=True`, `0.0.0.0`) |
| RNG-SAST-003 | CWE-798  | `ringnode/config.py` (hardcoded session secret + Redis password) |
| RNG-SAST-004 | CWE-79   | `ringnode/views/portal.py` (Markup with user content) |
| RNG-SAST-005 | CWE-22   | `ringnode/views/files.py` (`send_from_directory` with `..`) |
| RNG-SAST-006 | CWE-918  | `ringnode/services/charging.py` (urllib on user URL) |
| RNG-SAST-007 | CWE-78   | `ringnode/services/sim.py` (`os.system` with MSISDN) |
| RNG-SAST-008 | CWE-916  | `ringnode/auth.py` (`hashlib.sha256` for password storage, no salt) |
| RNG-SAST-009 | CWE-209  | `ringnode/views/api.py` (`Exception` + `repr` returned to client) |
| RNG-SAST-010 | CWE-352  | `ringnode/app.py` (`WTF_CSRF_ENABLED=False`) |

## IaC (6)
- RNG-IAC-001 ElastiCache Redis with `transit_encryption_enabled=false` (`infra/terraform/redis.tf`)
- RNG-IAC-002 ElastiCache Redis no AUTH token (`infra/terraform/redis.tf`)
- RNG-IAC-003 SG ingress 6379 from anywhere (`infra/terraform/main.tf`)
- RNG-IAC-004 Container runs as root, no HEALTHCHECK (`Dockerfile`)
- RNG-IAC-005 K8s `runAsNonRoot: false` + capabilities NET_RAW added (`infra/k8s/deployment.yaml`)
- RNG-IAC-006 K8s ConfigMap stores secret (`infra/k8s/configmap.yaml`)

## SCA (4)
| ID | Package | Version | CVE |
|---|---|---|---|
| RNG-SCA-001 | Flask        | 1.0.2   | CVE-2018-1000656 |
| RNG-SCA-002 | Werkzeug     | 0.14.1  | CVE-2019-14806 |
| RNG-SCA-003 | redis        | 3.5.3   | CVE-2023-28858 |
| RNG-SCA-004 | requests     | 2.20.0  | CVE-2023-32681 |

## Pipeline (3)
- RNG-CI-001 Hardcoded Carrier API key (`.github/workflows/ci.yml`)
- RNG-CI-002 No permissions block
- RNG-CI-003 Slack incoming webhook URL hardcoded for failure notification
