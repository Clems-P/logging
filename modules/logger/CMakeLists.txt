# modules/logger/CMakeLists.txt
add_library(logger STATIC logging.c)
target_include_directories(logger PUBLIC .)


set(SCRIPT_PATH "${CMAKE_CURRENT_LIST_DIR}/scripts/extract_dico.py")
set_target_properties(logger PROPERTIES LOGGER_SCRIPT_PATH "${SCRIPT_PATH}")

function(logger_generate_dictionary TARGET_NAME)
    # On récupère la propriété depuis la cible 'logger'
    get_target_property(EXTRACT_SCRIPT logger LOGGER_SCRIPT_PATH)

    add_custom_command(
        TARGET ${TARGET_NAME}
        POST_BUILD
        COMMAND "${Python3_EXECUTABLE}" "${EXTRACT_SCRIPT}" 
                "$<TARGET_FILE:${TARGET_NAME}>" 
                "${CMAKE_BINARY_DIR}/dictionary.json"
        COMMENT "Extraction du dictionnaire de logs depuis l'ELF..."
        VERBATIM
    )
endfunction()