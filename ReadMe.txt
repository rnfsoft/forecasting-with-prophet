Tutorial from
    https://towardsdatascience.com/forecasting-with-prophet-d50bbfe95f91

avocado.csv from 
    https://www.kaggle.com/neuromusic/avocado-prices

For Windows 10
    Install mini conda
    VS Code Terminal
        conda create -n fbprophet python=3.7
        close open Terminal
        Ctrl + Shift + P: Select Interpreter then select conda('base': conda)
        deactivate: (base) conda
        conda activate fbprophet
        conda install libpython m2w64-toolchain -c msys2
        follow instruction https://pystan.readthedocs.io/en/latest/windows.html#setting-up-mingw-w64-on-windows
        pip install fbprophet

    script.py
        ModuleNotFoundError: No module named ‘pandas’ (conda environment): conda remove pandas --> conda install pandas
