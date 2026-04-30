# CMakeLists.txt (Racine)
cmake_minimum_required(VERSION 3.10)
project(TestLogger C)

set(CMAKE_C_STANDARD 11)

# --- Gestion Automatique du Venv ---
set(VENV_DIR "${CMAKE_CURRENT_SOURCE_DIR}/project_venv")

if(NOT EXISTS "${VENV_DIR}/pyvenv.cfg")
    message(STATUS "Venv non trouvé. Création en cours dans ${VENV_DIR}...")
    
    # 1. Création du venv
    execute_process(
        COMMAND python3 -m venv "${VENV_DIR}"
        RESULT_VARIABLE venv_rc
    )
    
    if(NOT venv_rc EQUAL 0)
        message(FATAL_ERROR "Impossible de créer le venv python.")
    endif()

    # 2. Installation des dépendances (pyelftools)
    message(STATUS "Installation des dépendances dans le venv...")
    execute_process(
        COMMAND "${VENV_DIR}/bin/pip" install pyelftools
        RESULT_VARIABLE pip_rc
    )
    
    if(NOT pip_rc EQUAL 0)
        message(FATAL_ERROR "Erreur lors de l'installation de pyelftools.")
    endif()
endif()

set(Python3_EXECUTABLE ${CMAKE_CURRENT_SOURCE_DIR}/project_venv/bin/python3)
find_package(Python3 REQUIRED)

# Inclure le module
add_subdirectory(modules/logger)

# Créer l'exécutable
add_executable(app_test main.c)

# Lier au module
target_link_libraries(app_test PRIVATE logger)

# Activer la génération du dictionnaire pour cet exécutable
logger_generate_dictionary(app_test)