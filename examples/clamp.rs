// stone:job stone:util.clamp
// stone:function clamp_rs

#[no_mangle]
pub extern "C" fn clamp_rs(value: i32, minimum: i32, maximum: i32) -> i32 {
    if value < minimum {
        return minimum;
    }
    if value > maximum {
        return maximum;
    }
    value
}
