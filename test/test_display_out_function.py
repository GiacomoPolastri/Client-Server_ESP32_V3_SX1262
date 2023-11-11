def test_display_out():
    # Crea un oggetto DISPLAY_OUT con alcune righe di test
    rows = ["Test Line 1", "Test Line 2", "Test Line 3"]
    display = DISPLAY_OUT(*rows)

    # Verifica che l'oggetto sia stato creato correttamente
    assert display.rows == rows

    # Verifica che la funzione display_out abbia chiamato correttamente i metodi della libreria OLED
    # Puoi fare ciò creando una classe mock della libreria SSD1306_I2C
    class MockSSD1306_I2C:
        def __init__(self, width, height, i2c):
            self.width = width
            self.height = height
            self.i2c = i2c
            self.display_data = []

        def fill(self, value):
            # Simula la funzione fill della libreria originale
            pass

        def text(self, text, x, y):
            # Simula la funzione text della libreria originale
            self.display_data.append((text, x, y))

        def show(self):
            # Simula la funzione show della libreria originale
            pass

    # Sostituisci la classe originale con la classe mock
    original_SSD1306_I2C = globals()["SSD1306_I2C"]
    globals()["SSD1306_I2C"] = MockSSD1306_I2C

    try:
        # Esegui la funzione display_out
        display.display_out()

        # Verifica che la libreria OLED sia stata utilizzata correttamente
        mock_oled = MockSSD1306_I2C(SET_OLED_WIDTH, SET_OLED_HEIGHT, None)
        assert mock_oled.display_data == [("Test Line 1", 0, 0), ("Test Line 2", 0, 20), ("Test Line 3", 0, 40)]

    finally:
        # Ripristina la classe originale alla fine dei test
        globals()["SSD1306_I2C"] = original_SSD1306_I2C

# Esegui i test
test_display_out()
