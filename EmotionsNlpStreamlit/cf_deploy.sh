TEMPLATE_FILE_PATH=final.yaml
STACK_NAME=CF-NLP-STACK
TAG_KEY=NLP-APP
TAG_VALUE=STREAMLIT-NLP

aws cloudformation deploy --template-file ${TEMPLATE_FILE_PATH}  --stack-name ${STACK_NAME} --tags ${TAG_KEY}=${TAG_VALUE}