use serde::{Serialize, Deserialize};
use serde_json::Result;

#[derive(Serialize, Deserialize)]
struct Profile {
    name: String
}

pub fn create_profile(name: &String) {
    let profile_struct = Profile {
        name: name.to_string()
    };
    println!("{}", profile_struct.name)
}