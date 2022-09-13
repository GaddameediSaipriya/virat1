mkdir -p ~/.sreamlit/

echo "\
[server]\n\
headless = true\n\
port = $Port\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
