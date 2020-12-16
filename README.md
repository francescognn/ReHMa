# ReHMa


Io creerei un runner che abbia un Init, una step e una shutdown functions e la creerei come classe virtuale, per poi avere due classi che ereditano da questa: 
    - platform_runner (che userà librerie che possono girare solo su Raspberry per esempio GPIO) 
    - agnostic_runner (che farà le stesse cose ma con interfacce stubbate, dovremmo quindi creare un generatore di reader e un writer)
Per quanto riguarda il testing io farei: 
    - unit tests (che testano le singole funzioni), ne ho creato uno di esempio
    - integration tests (test più completi che fanno girare tutto il codice simulando input e output

Il platform_runner girerà sulla Raspberry mentre il agnostic_runner girerà solo per poter fare gli integration tests stubbundo input e output
