#!/usr/bin/env bash

dropdb trivia_test
createdb trivia_test

psql trivia_test < trivia.psql