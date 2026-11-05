// stone:job stone:math.saturate
// stone:function saturate_rs

#[no_mangle]
pub extern "C" fn saturate_rs(value: f64) -> f64 {
    if value < 0.0 {
        return 0.0;
    }
    if value > 1.0 {
        return 1.0;
    }
    value
}
