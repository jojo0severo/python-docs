import logging


def basic_logging():
    logging.debug('Debug')
    logging.info('Info')
    logging.warning('Warning')


def better_logging_strategy():
    """
    É melhor o uso da função getLogger para criar um objeto logger
    e usar esse objeto para fazer os logs, caso contrário será utilizado
    o logger raiz que pode não ser o mesmo que você espera.
    """ 
    logger = logging.getLogger('get_logger')
    
    # não envia pro root também, por padrão as mensagens são propagadas para todos os loggers "pais"
    logger.propagate = False  
    
    logger.setLevel(logging.INFO)
    logger.debug("debug") # não irá printar devido ao log level
    logger.info("info")
    logger.warning("warning")


def example_with_file_handler():
    """
    File handler é um objeto que escreve logs em um arquivo
    """
    file_handler = logging.FileHandler("example.log")
    logger = logging.getLogger('file_handler')
    
    # não envia pro root também, por padrão as mensagens são propagadas para todos os loggers "pais"
    logger.propagate = False  

    logger.addHandler(file_handler)
    logger.warning("warning")


def example_with_stream_handler():
    """
    Stream handler é um objeto que escreve logs em um stream
    """
    stream_handler = logging.StreamHandler()
    logger = logging.getLogger('stream_example')
    
    # não envia pro root também, por padrão as mensagens são propagadas para todos os loggers "pais"
    logger.propagate = False  

    logger.addHandler(stream_handler)
    logger.warning("warning")


def example_formatter():
    """
    Formatter é um objeto que formata a mensagem de log
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger = logging.getLogger('formatter_example')

    # não envia pro root também, por padrão as mensagens são propagadas para todos os loggers "pais"
    logger.propagate = False  

    logger.addHandler(stream_handler)
    logger.warning("warning")



basic_logging()
better_logging_strategy()
example_with_file_handler()
example_with_stream_handler()
example_formatter()
