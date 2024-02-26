# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st

st.set_page_config(page_title="Actividad diaria", page_icon="📊")
st.markdown("# Actividad diaria")
st.sidebar.header("Actividad diaria")

import streamlit as st

# Inicializar el contador
contador = st.session_state.get('contador', 0)

# Crear una fila para mostrar los botones
st.write("Nuevo prospecto")
col1, col2 = st.columns([1, 1])

# En la primera columna, mostrar el botón "más"
with col1:
    if st.button('más'):
        if contador <= 25:  # Verificar que el contador no exceda el máximo de 25 puntos
            contador += 1
            st.session_state['contador'] = contador

# En la segunda columna, mostrar el botón "menos"
with col2:
    if st.button('menos'):
        if contador > 0:  # Verificar que el contador no sea menor a 0 puntos
            contador -= 1
            st.session_state['contador'] = contador


# Mostrar el contador actual
st.write(f'Contador actual: {contador} puntos')

# Crear un botón que reinicie el contador
if st.button('Reiniciar contador'):
    contador = 0
    st.session_state['contador'] = contador