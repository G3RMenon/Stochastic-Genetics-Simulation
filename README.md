# Stochastic Foundations of Genetic Diffusion

This repository contains a numerical implementation of the **Wright-Fisher Diffusion Model**, a fundamental framework in population genetics used to describe the stochastic movement of allele frequencies over time.

## Theoretical Context
The change in allele frequency $p$ is modeled as a Stochastic Differential Equation (SDE):
$$dp = \sqrt{\frac{p(1-p)}{2N}} dW_t$$

Where:
- $p$ is the allele frequency.
- $N$ is the effective population size.
- $dW_t$ represents the standard Wiener process (Gaussian noise).

## Implementation Details
The simulation utilizes the **Euler-Maruyama method** for the numerical integration of the SDE. This "forward" diffusion process is a mathematical prerequisite for understanding the "backward" genealogical merging (coalescent theory) required for generative modeling in discrete sequence data.

## Relevance to Generative AI
Understanding the forward transition density of genetic data is critical for designing principled denoising kernels in diffusion-based generative models.
