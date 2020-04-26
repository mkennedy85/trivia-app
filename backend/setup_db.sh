#!/usr/bin/env bash

dropdb trivia
createdb trivia

psql trivia < trivia.psql