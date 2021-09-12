library(dplyr)

data <- read.csv("BD_prueba.csv", encoding = "UTF-8", nrows = 85)

names(data) <- c("n_nombres", "n_apellido1", "n_apellido2", "k_cedula",
                 "f_nacimiento", "i_genero", "f_ingreso", "o_numero", "o_cargo",
                 "o_jefe", "o_zona", "n_municipio", "n_departamento", "v_ventas2019",
                 "o_email", "o_clave", "o_imagen", "o_telefono")

library(lubridate)

data <- data %>% mutate(f_nacimiento = format(as.Date(f_nacimiento, "%d/%m/%Y"), "%Y-%m-%d")) %>%
   mutate(f_ingreso = format(as.Date(f_ingreso, "%d/%m/%Y"), "%Y-%m-%d")) 

data <- data %>% mutate(k_cedula = gsub("\\.", "", k_cedula)) %>%
   mutate(v_ventas2019 = gsub("\\$", "", v_ventas2019)) %>%
   mutate(v_ventas2019 = sub("\\.", "", v_ventas2019)) %>%
   mutate(o_telefono = gsub("-", "", o_telefono)) %>%
   mutate(v_ventas2019 = as.numeric(v_ventas2019)) %>% mutate(o_telefono = as.numeric(o_telefono)) %>%
   mutate(k_cedula = as.numeric(k_cedula))

which(is.na(data$v_ventas2019))
data[which(is.na(data$v_ventas2019)), ]$v_ventas2019 = 0.000

View(data)

write.csv(x = data, file = "BD_Datos.csv", row.names = F)
