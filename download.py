def download_online_model(url, dir_name):
    print(f"[~] Downloading voice model with name {dir_name}...")
    zip_name = url.split("/")[-1]
    extraction_folder = os.path.join(m.rvc_models_dir, dir_name)
    if os.path.exists(extraction_folder):
        print(f"Voice model directory {dir_name} already exists! Skipping download.")
        return

    if "https://" in url:
        url = f"https://pixeldrain.com/api/file/{zip_name}"


    import requests, zipfile, io
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(os.path.join(extraction_folder, os.path.basename(zip_name.split(".zip")[0]))
    # print("[+] Model successfully downloaded!")


    # original download script
    # urllib.request.urlretrieve(url, zip_name)
    # print("[~] Extracting zip - {zip_name}")
    # with zipfile.ZipFile(zip_name, "r") as zip_ref:
    #    for member in zip_ref.infolist():
    #        # skip directories
    #        if member.is_dir():
    #            continue
            # create target directory if it does not exist
    #        os.makedirs(extraction_folder, exist_ok=True)
            # extract only files directly to extraction_folder
    #        with zip_ref.open(member) as source, open(
    #            os.path.join(extraction_folder, os.path.basename(member.filename)), "wb"
    #        ) as target:
    #            shutil.copyfileobj(source, target)
    # print(f"[+] {dir_name} Model successfully downloaded!")