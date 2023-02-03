use std::fs;
use std::path::Path;

pub fn create_profile_file(data: &String) {
    fs::create_dir_all("profiles").expect("Error while creating directory");

    let path = "./profiles/";
    fs::write(path.to_owned() + "test2" + ".json", data).expect("Error while creating file");
}

pub fn read_profile_directory() {
    let path = fs::read_dir("./profiles/").unwrap();
    for files in path {
        println!("{}", files.unwrap().path().display())
    }
}

pub fn remove_profile_file() {

}