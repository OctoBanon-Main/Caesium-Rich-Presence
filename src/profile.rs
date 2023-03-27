use serde::{Serialize, Deserialize};
use serde_json::Result;

use crate::filesystem::{create_profile_file};

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

pub fn create_profile(name: &String) -> Result<()> {
    let profile_data = Profile {
        client_id: 1,
        details: "Test".to_owned(),
        state: "Test".to_owned(),
        start_timestamp: false,
        end_timestamp: 0,
        large_image_url: "".to_owned(),
        small_image_url: "".to_owned(),
        large_image_text: "".to_owned(),
        small_image_text: "".to_owned()
    };

    let json = serde_json::to_string_pretty(&profile_data)?;
    create_profile_file(&name, &json);

    Ok(())
}