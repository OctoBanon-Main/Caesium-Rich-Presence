use std::fs;

use serde::{Serialize, Deserialize};
use serde_json::Result;


#[derive(Serialize, Deserialize)]
struct Profile {
    client_id: u64,
    details: String,
    state: String,
    start_timestamp: bool,
    end_timestamp: u64,
    large_image_url: String,
    small_image_url: String,
    large_image_text: String,
    small_image_text: String,
}

pub fn create_profile() -> Result<()> {
    let data = r#"{"client_id": 1,
            "details": "Test",
            "state": "Test",
            "start_timestamp": true,
            "end_timestamp": 1337,
            "large_image_url": "Test",
            "small_image_url": "Test",
            "large_image_text": "Test",
            "small_image_text": "Test",
            "party_size": [
                1,
                5
            ]
        }"#;

    fs::create_dir_all("../profiles").expect("TODO: panic message");
    let path = "./profiles/";

    let json = serde_json::to_string_pretty(&data)?;
    fs::write(path.to_owned() + "test" + ".json", json).expect("TODO: panic message");

    Ok(())
}

pub fn load_profile_list() {
    
}

// pub fn remove_profile() {
//     let input = input_reader::input::read("You really wanna remove this profile? (Y/N)");
//     match input.as_str() {
//         "y" | "Y" => {
//             let path = Path::new("./profiles/").join(_name.to_owned() + ".json").exists();
//             // if path == true {
//             //     fs::remove_file(path.to_string()).expect("TODO: panic message");
//             // }
//             println!("{:?}", path)
//         },
//         "n" | "N" => println!("No"),
//         _ => println!("Error: Unknown input!")
//     }
// }