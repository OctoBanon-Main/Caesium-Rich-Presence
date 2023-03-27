use std::fs;

pub fn create_profile_file(name: &String, data: &String) {
    fs::create_dir_all("profiles").expect("Error while creating directory");

    let path = "./profiles/";
    fs::write(path.to_owned() + &name + ".json", data).expect("Error while creating file");
}