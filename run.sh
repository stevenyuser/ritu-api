#!/bin/bash

############ RUN SERVER #############
RUN_SERVER()
{
    if [ -n "$PORT" ]
    then
        PORT_=$PORT
    else
        PORT_=8080
    fi

    echo "Starting server on port $PORT_"

    # add --reload flag for auto reload during development
    uvicorn src.main:app --host 0.0.0.0 --port $PORT_ --reload
}

echo "Running Server..."

RUN_SERVER