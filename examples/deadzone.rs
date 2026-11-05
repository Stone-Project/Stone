// stone:job stone:math.deadzone
// stone:function deadzone_rs

#[no_mangle]
pub extern "C" fn deadzone_rs(value: f64, threshold: f64) -> f64 {
    let threshold = if threshold < 0.0 { -threshold } else { threshold };
    if value < 0.0 {
        if -value <= threshold { 0.0 } else { value }
    } else if value <= threshold {
        0.0
    } else {
        value
    }
}
