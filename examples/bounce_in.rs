// stone:job stone:math.bounce_in
// stone:function bounce_in_rs

#[no_mangle]
pub extern "C" fn bounce_in_rs(t: f64) -> f64 {
    fn bounce_out(t: f64) -> f64 {
        if t < 1.0 / 2.75 {
            7.5625 * t * t
        } else if t < 2.0 / 2.75 {
            let u = t - 1.5 / 2.75;
            7.5625 * u * u + 0.75
        } else if t < 2.5 / 2.75 {
            let u = t - 2.25 / 2.75;
            7.5625 * u * u + 0.9375
        } else {
            let u = t - 2.625 / 2.75;
            7.5625 * u * u + 0.984375
        }
    }
    1.0 - bounce_out(1.0 - t)
}
