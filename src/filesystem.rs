use std::fs;

pub fn create_profile_file(data: &String) {
    fs::create_dir_all("profiles").expect("Error while creating directory");

    let path = "./profiles/";
    fs::write(path.to_owned() + "test" + ".json", data).expect("Error while creating file");
}