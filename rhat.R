library(asbio)
genes = c("ATP6", "ATP8", "COX1", "COX2", "COX3", "CYTB", "ND1", "ND2", "ND3",
          "ND4", "ND4L", "ND5", "ND6")

df = data.frame(Gene = genes, Posterior = rep(NA, 13), Likelihood = rep(NA, 13),
                Prior = rep(NA, 13), alpha = rep(NA, 13), branch_rates = rep(NA, 13),
                er.1. = rep(NA, 13), er.2. = rep(NA, 13), er.3. = rep(NA, 13),
                er.4. = rep(NA, 13), er.5. = rep(NA, 13), er.6. = rep(NA, 13),
                gamma_rates.1. = rep(NA, 13), gamma_rates.2. = rep(NA, 13),
                gamma_rates.3. = rep(NA, 13), gamma_rates.4. = rep(NA, 13),
                pi.1. = rep(NA, 13), pi.2. = rep(NA, 13), pi.3. = rep(NA, 13),
                pi.4. = rep(NA, 13), TL = rep(NA, 13))
  
  
for(i in 1:length(genes)){  
  gene = genes[i]
  
  setwd(paste0('C:/Users/ben/Desktop/covarion/results/turtles/cov/', gene))
  
  run1 = read.table(paste0('cov_turtles_', gene, '_run_1.log'), header = TRUE)
  run2 = read.table(paste0('cov_turtles_', gene, '_run_2.log'), header = TRUE)
  run3 = read.table(paste0('cov_turtles_', gene, '_run_3.log'), header = TRUE)
  
  params = colnames(run1)
  
  for(j in params[-1]){
    M = matrix(NA, nrow = 7501, ncol = 3)
    M[,1] = run1[[j]]
    M[,2] = run2[[j]]
    M[,3] = run3[[j]]
    
    df[[j]][which(genes == gene)] = R.hat(M, burn.in = 0)
  }
}  
  
