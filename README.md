# AI Infra Engineer 🚀

Este repositório documenta minha jornada para me tornar **AI Infrastructure Engineer**, unindo minha bagagem de **DevOps / Platform Engineering** com o mundo de **AI/ML workloads em produção**.

## 🎯 Objetivo
Construir um portfólio hands-on que demonstre:
- Provisionamento de clusters GPU (Terraform + Kubernetes).
- Treinamento distribuído (PyTorch DDP, Ray).
- Deploy e serving de modelos (Triton, Hugging Face TGI).
- Observabilidade (Prometheus, Grafana).
- Segurança e custo-eficiência (spot instances, RBAC, network policies).

## 🪜 Roadmap
- **Fase 1 (0–3m):** Labs básicos – deploy de modelos pequenos, GPUs spot, monitoramento inicial.
- **Fase 2 (3–6m):** Treino distribuído, serving otimizado, pipelines CI/CD para AI.
- **Fase 3 (6–12m):** Multi-tenant clusters, segurança, arquitetura de AI infra completa.

## 📂 Estrutura
- `platform-labs/` → Labs de **Platform Engineer** (fallback seguro).
- `ai-infra-labs/` → Labs de **AI Infra Engineer** (foco principal).
- `infra-modules/` → Módulos reutilizáveis (Terraform, Helm).
- `docs/` → Arquiteturas, notas, otimizações.

## 🚀 Próximos passos
- [ ] Criar primeiro lab: deploy de modelo (Llama-2 7B quantizado) em K8s com Helm.
- [ ] Publicar dashboard de observabilidade (GPU/latência).
- [ ] Adicionar Terraform para provisionar instância GPU spot (AWS/GCP).

